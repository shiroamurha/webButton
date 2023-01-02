import PySimpleGUI as ui



def event_block(event):
    match event:
        case 'dump_settings':
            print('dumping... ')



frame_running = [
    ui.Frame('', [
        [ui.Text(f'Running... ', font='arial 12 bold', background_color='#23272a')]#🟢GREEN_CHECK_BASE64🔴RED_X_BASE64
    
    ], background_color='#23272a', vertical_alignment='t')
]



frame_output = [

    ui.Frame('Output', [
        [ui.Text('pipipo, fring, \nfrongs tongues \nbromgetersons. \nthe outputersons,', 
            font='arial 12 bold', text_color='white', background_color='black')]

    ], background_color='black', size=(250,125), border_width=0)
]



frame_buttons = ui.Frame('',[
    
    [ui.Sizer(1,8)],

    [ui.Button(
        'Connect', 
        font='verdana 19 bold', 
        button_color='black on #57f287', 
        size=(13,2), 
        border_width=0,
        focus=True,
        mouseover_colors=('#141414', '#2e8047')
    ), 

    ui.Push(background_color='#23272a'),

    ui.Button(
        'Disconnect', 
        font='verdana 19 bold', 
        button_color='black on #ed4245', 
        size=(13,2), 
        border_width=0,
        focus=True,
        mouseover_colors=('#141414', '#7a2223')
    )],

], vertical_alignment='c', size=(520, 110), background_color='#23272a', border_width=0)




frame_commands = [

    #[ui.Sizer(1,28)],
    [ui.Frame('Command Assets', [
        [   
            ui.Text('Button A', background_color='#23272a'), 
            ui.Input(key='command_button_a', text_color='white', default_text='a', size=(19, 5), background_color='#23272a')
        ],
        [
            ui.Text('Button B', background_color='#23272a'), 
            ui.Input(key='command_button_b', text_color='white', default_text='b', size=(19, 5), background_color='#23272a')
        ],
        [
            ui.Text('Button C', background_color='#23272a'), 
            ui.Input(key='command_button_c', text_color='white', default_text='c', size=(19, 5), background_color='#23272a')
        ],
        [
            ui.Text('Button D', background_color='#23272a'), 
            ui.Input(key='command_button_d', text_color='white', default_text='d', size=(19, 5), background_color='#23272a')
        ],

        [
            ui.Text('New Session', background_color='#23272a'), 
            ui.Radio(
                'True', 
                group_id=1, 
                text_color='#2a23c2', 
                font='bold', 
                key='new_session_True', 
                size=(3,1), 
                background_color='#23272a'
            ), 
            ui.Radio(
                'False', 
                group_id=1, 
                text_color='red', 
                font='bold', 
                key='new_session_False', 
                size=(4,1), 
                background_color='#23272a'
            )
        ],

        [ui.Ok('Dump settings', key='dump_settings', button_color='white on #4c555c')]
        
    ], background_color='#23272a')]
]

layout = [
    [
        ui.Frame('', [[
            
            ui.Column([
                frame_running, 
                frame_output, 
                [ui.HSep() for _ in range(4)]

            ], background_color='#23272a'),
            ui.Column(frame_commands, vertical_alignment='t', background_color='#23272a')

        ]], background_color='#23272a', border_width=0)

    ],
        
    [frame_buttons]

]


window = ui.Window('Web Button Inspector', layout, background_color='#23272a')

while True:

    event, values = window.read()

    if event == ui.WIN_CLOSED:
        break

    event_block(event)


window.close()