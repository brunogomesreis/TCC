function salvar() {
    console.log()
    if(TestaCPF(document.getElementById('cpfPaciente').value)) {
        const paciente={
            "nome": document.getElementById('nomePaciente').value,
            "nascimento": document.getElementById('nascimentoPaciente').value,
            "cpf": document.getElementById('cpfPaciente').value,
            "email": document.getElementById('emailPaciente').value,
        }

        console.log(paciente)
        $.post('/cadastro',{ data: JSON.stringify(paciente) })
        limparCamposTela()
        alert("Dados salvos com sucesso")
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

function mudaCampo(strCPF) {
    if(strCPF.length==0) {
        if(document.getElementById("cpfPacienteGroup").classList.contains('has-error')) {
            document.getElementById("cpfPacienteGroup").classList.remove('has-error');
        }
        if(document.getElementById("cpfPacienteGroup").classList.contains('has-success')) {
            document.getElementById("cpfPacienteGroup").classList.remove('has-success');
        }
    }
    else {
        if(TestaCPF(strCPF)) {
            if(document.getElementById("cpfPacienteGroup").classList.contains('has-error')) {
                document.getElementById("cpfPacienteGroup").classList.remove('has-error');
            }
            document.getElementById("cpfPacienteGroup").classList.add('has-success');
        }
        else {
            if(document.getElementById("cpfPacienteGroup").classList.contains('has-success')) {
                document.getElementById("cpfPacienteGroup").classList.remove('has-success');
            }
            document.getElementById("cpfPacienteGroup").classList.add('has-error');
        }
    }
}