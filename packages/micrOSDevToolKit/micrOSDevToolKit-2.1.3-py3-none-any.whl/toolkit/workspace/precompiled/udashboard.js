// API HELPER FUNCTION - get module exposed widgets

function moduleHelp(module) {
    // Get and Parse module widget help message
    let endpoint = `${module}/help/True`;
    console.log(`[API] Endpoint: ${endpoint}`)
    return restAPI(endpoint).then(commands => {
        //console.log(`Raw ${module} help: ${commands.result}`)
        // Replace all occurrences of \" with " in each string and parse each string into a JSON object
        const parsedWidgets = commands.result.map(item => {
            const cleanedItem = item.replace(/\\"/g, '"');      // Workaround...
            return JSON.parse(cleanedItem);
        });
        console.log(`Parsed ${module} help:`);
        console.log(parsedWidgets)
        return parsedWidgets
    }).catch(error => {
        console.error(error)
        return [];
    });
}

// PAGE GENERATION

function containerAppendChild(elements, container) {
    // Append list of elements into the container aka draw elements :D
    if (!elements || !container) {
        console.error("Inputs array or container element is missing.");
        return;}
    elements.forEach(function(element) {
        container.appendChild(element);});
}

function generateElement(type, data, options={}) {
    // type: slider, button, box, h1, h2, p, li, etc.
    // data: rest command
    var container = document.getElementById('dynamicContent');
    var element;
    paragraph = document.createElement('p');
    if (type.toLowerCase() === 'slider') {
        // Create slider widget
        sliderWidget(container, paragraph, data, options)
    } else if (type.toLowerCase() === 'button') {
        // Create button widget
        buttonWidget(container, paragraph, data, options)
    } else if (type.toLowerCase() === 'box') {
        // Create textbox widget
        textBoxWidget(container, paragraph, data, options)
    } else if (type.toLowerCase() === 'color') {
        // Create color palette widget
        colorPaletteWidget(container, paragraph, data, options)
    } else {
        // Create other elements
        element = document.createElement(type);
        element.textContent = data;
        containerAppendChild([paragraph, element], container);
    }
}

function craftModuleWidgets(module, widgets) {
    // Create ALL exposed module function widgets
    if (widgets.length === 0) {
        console.log(`${module} no exposed widgets`);
        return;
    }
    console.log(`Craft widgets bind to ${module}`);
    generateElement(type='h2', data=`🧬 ${module}`);
    // Check widget data struct for the given module
    widgets.forEach(item => {
        let type = item.type;
        let type_options = {};
        let lm_call = item.lm_call.replace(/\s/g, '/');

        let html_type='p';
        if (type === 'slider') {
            html_type='slider';
            type_options['range'] = item.range;
        } else if (type === 'button' || type === 'toggle') {
            html_type='button';
            type_options['range'] = item.range;
        } else if (type === 'textbox') {
            html_type = 'box'
        } else if (type === 'color') {
            html_type = 'color'
        } else {
            console.log(`Unsupported micrOS widget html_type: ${type}`)
            return;
        }
        generateElement(type=html_type, data=`${module}/${lm_call}`, options=type_options);
    })
}


function DynamicWidgetLoad() {
    // INIT DASHBOARD (load active modules -> build page)
    restAPI('modules').then(data => {
        //console.log(data);
        let app_list = data['result'];
        // Handle the app_list data here
        for (const module of app_list) {
            // NEW module widget query
            moduleHelp(module).then(widgets => {
                craftModuleWidgets(module, widgets)
            }).catch(error => {
                // You can work with parsedWidgets here
                console.error(error);
            });
        }
    }).catch(error => {
        console.error(error);
    });
}


function CustomWidgetLoad(endpoint) {
    // INIT DASHBOARD (load custom widget commands -> build page)
    // endpoint: 'dashboard_be/widget_list' returns special dict
    restAPI(endpoint).then(commands => {
        console.log(commands.result)
        const widget_dict=commands.result;
        var opts = {};
        opts.title_len = 3;
        for (const module in widget_dict) {
            if (Object.hasOwnProperty.call(widget_dict, module)) {
                const innerObject = widget_dict[module];
                generateElement(type='h2', data=`🧬 ${module}`);
                // Iterate through the inner object
                for (const func in innerObject) {
                    if (Object.hasOwnProperty.call(innerObject, func)) {
                        const api_type = innerObject[func];
                        const api_cmd = `${module}/${func}`;
                        console.log(`Gen custom Type: ${api_type} Cmd: ${api_cmd}`);
                        generateElement(type=api_type, data=api_cmd, options=opts);
        };};};}
    }).catch(error => {
        console.error(error);
    });
}

// craftModuleWidgets
