# webButton
flask app with weird shit. done with the purpose of communicating between cellphone and pc (cellphone -> server -> pc)
<br><br>

<h3>the papo eh o seguinte: </h3>
    <li>    o app_main.py é o app flask que fica rodando dentro do servidor, o static/ui.html é o html que o flask vai usar pra o index, os outros arquivos nao citados aqui sao so config do servidor</li>
    <li>    flask abre o html como objeto bsoup, a rota principal retorna o html como UI. </li>
    <li>    tem quatro botoes linkados respectivamente com cada uma das funçoes de rota do flask (a, b, c, d). </li>
    <li>    cada funçao de botao chama a funçao output com o parametro respectivo ao id do botao. </li>
    <li>    a funçao output acha a tag textarea#output e troca a string dela pelo id que a funçao recebe como parametro. </li>
    <li>    depois que uma funçao de botao eh chamada, o html da UI é atualizado pra o html modificado com a output nova. </li>
    <li>    a tag textarea#output é invisivel na UI, é oculta so pra ser encontrada no web scrapping que vai puxar apenas o html e pegar o valor da output.</li>
    <li>    o inspector.py é o script que vai ficar checando o html do site pra receber o valor da output quando o botao for pressionado. o state.json é a sessao do servidor pra poder acessar o bagulho (macaquice do host)</li>
