function salvar() {
    var nomeExperimento=document.getElementById('nomeExperimento').value;   
    var e=document.getElementById("listaNomePaciente");
    var cpf=e.options[e.selectedIndex].id;


    if(document.getElementById('exampleInputFile')&&document.getElementById('exampleInputFile').value) {
        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/experimento?cpf="+cpf+"&nome="+nomeExperimento,
            data: document.getElementById('exampleInputFile').files[0],
            processData: false, 
            contentType: false, 
            cache: false, 
            timeout: 600000, 
            success: function(data) {
                console.log(data);                
                $("#btnSubmit").prop("disabled",false);
            },
            error: function(e) {
                console.log(e);              
                $("#btnSubmit").prop("disabled",false);
            }
        });
    }
    

}