import PySimpleGUI as ui
import inspector 
from time import sleep
from datetime import datetime as date
        

def clock_tick():
    sleep(2)


inspect = inspector.Inspector()
commands_dict = inspect.get_commands()

frame_running = [
    ui.Frame('', [
        [
            ui.Text('Running...     ', key='running', font='arial 12 bold', background_color='#23272a'),
            #ui.Column([], size=(80, 1)),
            ui.Push(background_color='#23272a'),
            ui.Button('•', key='tick', size=(1,1))
        ]
    
    ], background_color='#23272a', size=(250,35), vertical_alignment='t')
]



frame_output = [

    ui.Frame('Output', [
        [ui.Text('', 
            key='output_frame',
            font='Consolas 10 bold', 
            text_color='white', 
            background_color='black',
            enable_events=True
        )]
    ], background_color='black', size=(250,125), border_width=0)
]



frame_buttons = ui.Frame('',[
    
    [ui.Sizer(1,8)],

    [ui.Button(
        'Connect', 
        key='connect',
        font='verdana 19 bold', 
        button_color='black on #57f287', 
        size=(14,2), 
        border_width=0,
        focus=True,
        mouseover_colors=('#141414', '#2e8047'),
        disabled_button_color=('#2f3438', None),
        disabled=True
    ), 

    ui.Push(background_color='#23272a'),

    ui.Button(
        'Disconnect', 
        key='disconnect',
        font='verdana 19 bold', 
        button_color='black on #ed4245', 
        size=(14,2), 
        border_width=0,
        focus=True,
        disabled_button_color=('#2f3438', None),
        mouseover_colors=('#141414', '#7a2223')
    )],

], vertical_alignment='c', size=(545, 110), background_color='#23272a', border_width=0)



frame_commands = [

    #[ui.Sizer(1,28)],
    [ui.Frame('Command Assets', [
        [   
            ui.Text('Button A', background_color='#23272a'), 
            ui.Input(
                key='command_button_a', 
                text_color='white', 
                default_text=commands_dict.get('a')[1], 
                size=(25, 5), 
                background_color='#23272a'
            )
        ],
        [
            ui.Text('Button B', background_color='#23272a'), 
            ui.Input(
                key='command_button_b', 
                text_color='white', 
                default_text=commands_dict.get('b')[1], 
                size=(25, 5), 
                background_color='#23272a'
            )
        ],
        [
            ui.Text('Button C', background_color='#23272a'), 
            ui.Input(
                key='command_button_c', 
                text_color='white', 
                default_text=commands_dict.get('c')[1], 
                size=(25, 5), 
                background_color='#23272a'
            )
        ],
        [
            ui.Text('Button D', background_color='#23272a'), 
            ui.Input(
                key='command_button_d', 
                text_color='white', 
                default_text=commands_dict.get('d')[1], 
                size=(25, 5), 
                background_color='#23272a'
            )
        ],

        [
            ui.Text('New Session', background_color='#23272a'), 
            ui.Radio(
                'True', 
                default = commands_dict.get('new_session'),
                group_id=1, 
                text_color='#2a23c2', 
                font='bold', 
                key='new_session_True', 
                size=(3,1), 
                background_color='#23272a'
            ), 
            ui.Radio(
                'False', 
                default = not commands_dict.get('new_session'), # if True: False; if False: True
                # that statement is a little funny xd
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
                [ui.HSep() for _ in range(4)], 
                frame_output, 
                [ui.HSep() for _ in range(4)]

            ], background_color='#23272a'),
            ui.Column(frame_commands, vertical_alignment='t', background_color='#23272a')

        ]], background_color='#23272a', border_width=0)

    ],
        
    [frame_buttons]

]



def event_block(event):
    global is_running
    global values
    match event:

        case 'tick':
            print('tick')

        case 'dump_settings':
            commands_dict['a'][1] = values['command_button_a']
            commands_dict['b'][1] = values['command_button_b']
            commands_dict['c'][1] = values['command_button_c']
            commands_dict['d'][1] = values['command_button_d']
            commands_dict['new_session'] = values['new_session_True']
            inspect.update_commands(commands_dict)
            
        case 'connect':
            window['disconnect'].update(disabled=False)
            window['connect'].update(disabled=True)
            #inspect.start()
            window['running'].update('Running...     ')
            is_running = True
            

        case 'disconnect':
            window['disconnect'].update(disabled=True)
            window['connect'].update(disabled=False)
            window['running'].update('Disconnected   ')
            is_running = False
            
        
window = ui.Window('Web Button Inspector', layout, background_color='#23272a')

is_running = True

inspect.start()

while True:

    if is_running:
        window.perform_long_operation(clock_tick, 'tick')

    event, values = window.read()
    event_block(event)
    
    if event == ui.WIN_CLOSED:
        inspect.close()
        break
    
    if is_running:
        output_value = inspect.loop()

    if is_running:
        if output_value is not None:

            if len(window['output_frame'].get()) == 0 or len(window['output_frame'].get())>174:

                window['output_frame'].update(f'Pressed: {output_value.upper()}     -     at [{str(date.now())[11:19]}]')

            else:

                window['output_frame'].update(f'{window["output_frame"].get()}\nPressed: {output_value.upper()}     -     at [{str(date.now())[11:19]}]')



window.close()
