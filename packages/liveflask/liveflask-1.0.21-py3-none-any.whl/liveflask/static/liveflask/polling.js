///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// POLLING
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


function init_polling(el) {
    let component_name = el.__liveflask['class']
    let retrieved_polls = attr_beginswith('live-poll', el);
    el.__liveflask['polls'] = [];
    let current_component;

    retrieved_polls.forEach(i => {
        current_component = i.parentNode.closest('[live-component]').getAttribute("live-component");
        if (current_component !== component_name) return;
        el.__liveflask['polls'].push(i)
    })


    el.__liveflask['polls'].forEach(i => {
        let property;
        let value;
        let modifier;


        [property, modifier, value] = get_model_prop_value(i, "live-poll")

        let method = property.split("(")[0];
        let args;
        let time;


        try {
            args = replace_undefined(property).match(/\(([^)]+)\)/)[1];
        } catch (e) {
            args = "__NOVAL__"
        }


        if (method === undefined) {
            method = "render"
        }


        [property, modifier, value] = get_model_prop_value(i, "live-poll-delay");
        if (property === undefined) {
            time = "2s"
        }
        time = property;

        (function () {
            setInterval(function () {
                send_request(el, {'method': method, "args": args}, i)
            }, parse_interval(time));
        })()
    })

}


