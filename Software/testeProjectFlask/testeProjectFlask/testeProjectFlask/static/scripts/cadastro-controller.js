function salvar() {
    console.log()
    if (TestaCPF(document.getElementById('cpfPaciente').value)){
        const paciente={
            "nome": document.getElementById('nomePaciente').value,
            "nascimento": document.getElementById('nascimentoPaciente').value,
            "cpf": document.getElementById('cpfPaciente').value,
            "email": document.getElementById('emailPaciente').value,
        }

        console.log(paciente)
        $.post('/cadastro',{ data: JSON.stringify(paciente) })
        limparCamposTela()
    }
    else
        alert("CPF invalido")
}

function limparCamposTela() {
    document.getElementById('nomePaciente').value="";
    document.getElementById('nascimentoPaciente').value="";
    document.getElementById('cpfPaciente').value="";
    document.getElementById('emailPaciente').value="";
}

function TestaCPF(strCPF) {
    var Soma;
    var Resto;
    Soma=0;
    if(strCPF=="00000000000") return false;

    for(i=1;i<=9;i++) Soma=Soma+parseInt(strCPF.substring(i-1,i))*(11-i);
    Resto=(Soma*10)%11;

    if((Resto==10)||(Resto==11)) Resto=0;
    if(Resto!=parseInt(strCPF.substring(9,10))) return false;

    Soma=0;
    for(i=1;i<=10;i++) Soma=Soma+parseInt(strCPF.substring(i-1,i))*(12-i);
    Resto=(Soma*10)%11;

    if((Resto==10)||(Resto==11)) Resto=0;
    if(Resto!=parseInt(strCPF.substring(10,11))) return false;
    return true;
}


$(document).ready(function() {
    $("#cpfPaciente").mask("999.999.999-99");
});
