
$(document).ready(function() {
    $('#nomeExperimento').popover({
        html: true,
        content: function() {
            return $('#experimento-popover-content').html();
        }
    });
    $('#nomePaciente').popover({
        html: true,
        content: function() {
            return $('#paciente-popover-content').html();
        }
    });
});

function changePatient(e) {
    document.getElementById('nomePaciente').innerText=e.innerText
}

function changeExperiment(e) {
    document.getElementById('nomeExperimento').innerText=e.innerText
}

function gerarGraficoOriginal() {
    nomeExperimento=document.getElementById('nomeExperimento').innerText
    nomePaciente=document.getElementById('nomePaciente').innerText
    $.post("/home?paciente="+nomePaciente+"&experimento="+nomeExperimento,function(data) {
        console.log(data);
        var data2=JSON.parse(data)
        Plotly.newPlot('bargraph',data2,{});
    });
}
