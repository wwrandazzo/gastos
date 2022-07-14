$(document).ready(function() {
    //Cargar ano actual
    var fecha = new Date();
    var ano = fecha.getFullYear();
    $("#selectano").val(ano);
    //Cargar mes actual
    var mes = fecha.getMonth();
    const mesNombres =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
    var nombremesactual = mesNombres[mes];
    $("#selectmes").val(nombremesactual);

    $("#btnBuscarGasto").click(function(e){
        e.preventDefault();
        meslistado = $("#selectmes").val();
        anolistado = $("#selectano").val();
        window.location ="/buscalist/"+meslistado+"/"+anolistado+"/";
    });

    $(".nivelcategoria").click(function(e){
        e.preventDefault();
        categoriasel = $(this).text();
        $("#id_categoria").val(categoriasel);
    });

});