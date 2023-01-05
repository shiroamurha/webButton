# webButton
flask app with weird shit. done with the purpose of communication between cellphone and pc (cellphone -> server -> pc)

> server host: wayscript
<h2>how it works: </h2>
    <li>    o app_main.py é o app flask que fica rodando dentro do servidor, o static/ui.html é o html que o flask vai usar pra o index, os outros arquivos nao citados aqui sao so config do servidor</li>
    <li>    flask abre o html como objeto bsoup, a rota principal retorna o html como UI. </li>
    <li>    tem quatro botoes linkados respectivamente com cada uma das funçoes de rota do flask (a, b, c, d). </li>
    <li>    cada funçao de botao chama a funçao output com o parametro respectivo ao id do botao. </li>
    <li>    a funçao output acha a tag textarea#output e troca a string dela pelo id que a funçao recebe como parametro. </li>
    <li>    depois que uma funçao de botao eh chamada, o html da UI é atualizado pra o html modificado com a output nova. </li>
    <li>    a tag textarea#output é invisivel na UI, é oculta so pra ser encontrada no web scrapping que vai puxar apenas o html e pegar o valor da output.</li>
    <li>    o inspector.py é o script que vai ficar checando o html do site pra receber o valor da output quando o botao for pressionado. o state.json é a sessao do servidor pra poder acessar o bagulho (macaquice do host)</li>
<h2>how to use: </h2>
<li>1- download the repository</li>
<li>2- you need to set up some dependencies, so at command prompt you must do <code>pip install PySimpleGUI</code>, <code>pip install playwright</code> and then <code>playwright install webkit</code>
<li>3- in static/commands.json you can put as many commands you want (in batch/shell language) assigned to the button you want following this pattern</li>

    > "a": ['command1'], "b": ["command2", "command3"]

<li>4- run (at the respective file path) <code>py inspector.py</code> to start the script to check the button output</li>
<li>5- press the button you want to at <a href="https://glamorously-beautiful-iris-flat-dev.wayscript.cloud/?">this website</a> </li>
