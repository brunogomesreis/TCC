function salvar() {

    var e=document.getElementById("listaNomePaciente");
    var cpf=e.options[e.selectedIndex].id;

    email=$.get('/teste/'+cpf,function(data) {
        alert(data);
    })
}