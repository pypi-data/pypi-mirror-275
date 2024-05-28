import hashlib
import json
import pprint
import secrets
from typing import Any

from flask import render_template_string
from markupsafe import Markup

from ..utils import to_class
from ..traits.has_synthesizer import Synthesizer


class HasSnapshots:
    def hydrate(self, obj, data: dict[str, Any]):
        if isinstance(data, str):
            # Assume data is a JSON string
            data = json.loads(data)
        # Convert types based on type hints
        if obj:
            try:
                annotations = obj.__annotations__
                for field_name, field_type in annotations.items():
                    if field_name in data and isinstance(data[field_name], str):
                        try:
                            data[field_name] = field_type(data[field_name])
                        except ValueError:
                            pass  # or handle the error as needed
                return obj(**data)
            except AttributeError:
                return data
        return data


    def from_snapshot(self, req_snapshot: dict[str, Any]):
        req_checksum: str = req_snapshot['snapshot']['checksum']
        del req_snapshot['snapshot']['checksum']
        if 'children' in req_snapshot['snapshot']:
            del req_snapshot['snapshot']['children']
        if 'models' in req_snapshot['snapshot']:
            del req_snapshot['snapshot']['models']
        if 'actions' in req_snapshot['snapshot']:
            del req_snapshot['snapshot']['actions']
        if 'polls' in req_snapshot['snapshot']:
            del req_snapshot['snapshot']['polls']
        # pprint.pprint(req_snapshot['snapshot'])

        source_checksum: str = hashlib.md5(
            json.dumps(req_snapshot['snapshot'], sort_keys=True, ensure_ascii=True, cls=Synthesizer).encode('utf-8')).hexdigest()

        # TODO: Implement checksum verification
        # if source_checksum != req_checksum:
        #     raise Exception("Stop trying to hack me.")


        class_name: str = req_snapshot['snapshot']['class']
        fqdn: str = req_snapshot['snapshot']['fqdn']
        data: dict[str, Any] = req_snapshot['snapshot']['data']
        # children = req_snapshot['snapshot']['children']

        _class: Any = to_class(fqdn)()
        _class.__name__, _class.__class__.__name__ = class_name, class_name
        if getattr(_class, "key", None):
            #print("checking if component key is set.......")
            key = getattr(_class, "key")
            #print(f"found key {key}")
        else:
            key = f"mvlive_{_class.__name__.lower()}_{secrets.token_urlsafe(4)}"
        setattr(_class, "key", key)

        for prop in data.items():
            setattr(_class, prop[0], prop[1])

        props = self.get_props(_class)

        class_annotations = _class.__annotations__
        for key in list(props.keys()):
            try:
                property_class = class_annotations.get(key)
                props[key] = self.hydrate(property_class, props[key])
            except json.JSONDecodeError:
                pass
            except TypeError:
                pass
        return _class

    def to_snapshot(self, _class: Any, component_fqdn):
        props: dict[str, Any] = self.get_props(_class)

        # loop through props and if any key matches a key in _class.mvlive__url, add the key value pair to props[url]
        if hasattr(_class, "mvlive__url"):
            props["url"] = {}
            for key in _class.mvlive__url:
                props["url"].update({key: props[key]})



        _class.key = props.get("key")

        # remove all keys from props that begin with '_' or '__'
        # for key in list(props.keys()):
        #     if key.startswith("_"):
        #         del props[key]

        #print(props)
        if _class.render.__doc__ is None:
            html: str = _class.render(
                props | {"this": Markup(f"document.getElementById('{ _class.key }').__liveflask")}
            )
        else:
            html: str = render_template_string(
                _class.render.__doc__,
                **props
            )

        # meta = self.dehydrate_properties(props)

        key = getattr(_class, "key", "")

        if "relationship_result_set" in props:
            del props["relationship_result_set"]

        if "result_set" in props:
            del props["result_set"]



        # loop through props and remove any methods
        for key in list(props.keys()):
            if callable(props[key]):
                #print(key)
                del props[key]


        snapshot: dict[str, Any] = {
            "class": _class.__class__.__name__,
            "fqdn": component_fqdn,
            "key": key,
            "data": props,
            # "html": html,
        }

        snapshot['checksum']: str = hashlib.md5(
            json.dumps(snapshot, sort_keys=True, ensure_ascii=True, cls=Synthesizer).encode('utf-8')).hexdigest()

        return html, snapshot
