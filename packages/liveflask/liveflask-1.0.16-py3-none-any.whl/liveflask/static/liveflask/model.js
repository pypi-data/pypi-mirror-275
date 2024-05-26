///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MODELS
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function init_model(el) {
    let component_name = el.__liveflask['class']
    //el.__liveflask['children'] = attr_beginswith('live-component', el);
    let retrieved_models = attr_beginswith('live-model', el);
    el.__liveflask['models'] = [];
    let current_component;

    retrieved_models.forEach(i => {
        current_component = i.parentNode.closest('[live-component]').getAttribute("live-component");
        if (current_component !== component_name) return;
        el.__liveflask['models'].push(i)
    })


    el.__liveflask['models'].forEach((i, index) => {
        let property;
        let value;
        let modifier;


        [property, modifier, value] = get_model_prop_value(i, "live-model")


        if (property.includes('lazy')) {
            i.addEventListener('change', event => {
                send_request(el, {update_property: [property.split("|")[1], $(i).val()]}, i)
            })
        }

        if (property.includes('debounce')) {
            var time = property.split("|")[0].match(/\(([^)]+)\)/)[1]
            const debounceModel = _.debounce((el, payload, target) => {
                send_request(el, payload, target);
            }, parse_interval(time))
            i.addEventListener('input', event => {
                debounceModel(el, {update_property: [property.split("|")[1], $(i).val()]}, i);
            })
        }

        if (!property.includes('|')) {
            i.addEventListener('input', event => {
                send_request(el, {update_property: [property, $(i).val()]}, i)
            })
        }
    })

}

function update_liveflask_model_attributes(el) {
    let data = el.parentNode.closest("[live-component]").__liveflask.data

    attr_beginswith('live-model', el).forEach(e => {
        [attribute, raw_attribute, modifier, time, property, value] = parse_liveflask_attributes(e, "live-model")
    })
}

