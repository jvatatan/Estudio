
// $(document).ready(function(e){
//     $("buscar_perfilUsuario").submit(function(e){
//         e.preventDefault();

//         $.ajax({
//             url: $(this).attr('action'),
//             type: $(this).attr('method'),
//             data: $(this).serialize(),

//             success: function(json){
//                 console.log(json)
//             }
//         })
//     })
// })
// function medicamento(){
//     buscar_medicamento = document.getElementById("buscar_medicamento").value
//     $.ajax({
//         url:"/medicamentos/buscarMedicamento/",
//         type:"GET",
//         data:{
//             asignacionColor : buscar_medicamento,
//         },
//         success: function(json){
//             console.log(json);
           
//         }
//     })
// }



/* $(function(){
    $('#store').empty();
    $.ajax({
        url: '/medicamentos/buscarMedicamento/',
        type: 'GET',
        success: function (json) {
            var asignacionBusquedahtml = '';
            for (var i = 0; i < json.length; i++) {
                asignacionBusquedahtml += '<tr role="row" class="odd" id="registro_item" style="background-color:rgb(255, 30, 30);">   <td style="color:Black;"><b>' + json[i].nombre +'</b></td>    <td style="color:Black;"><b>' + json[i].fecha_vencimiento + '</b></td>   <td style="color:Black;"><b>' + json[i].fabricado_por + '</b></td>   <td style="color:Black;"><b>' + json[i].registro_invima +'</b></td>   <td style="color:Black;"><b>' + json[i].numero_lote +'</b></td>   <td style="color:Black;"><b>'  + json[i].presentacion_comercial +'</b></td>   <td style="color:Black;"><b>'  + json[i].forma_farmaceutica +'</b></td>   <td style="color:Black;"><b>'  + json[i].principio_activo +'</b></td>   <td style="color:Black;"><b>'  + json[i].unidad_medica +'</b></td>   <td style="color:Black;"><b>' + json[i].porcentaje +'</b></td>   <td style="color:Black;"><b>'  + json[i].temperatura +'</b></td>   <td style="color:Black;"><b>' + json[i].cantidad +'</b></td>   <td style="color:Black;"><b>' + json[i].codigo +'</b></td>   <td style="background-color:rgb(255, 255, 255);"> </div> </div> <a href="{% url "actualizarMedicamento" medicamentos.id %}" data-toggle="tooltip" title="Actualizar Medicamento">   <button class="btn btn-primary btn-sm"><i class="fa fa-edit"></i></button></a>   <a href="{% url "eliminarMedicamento" medicamentos.id %}" data-toggle="tooltip" title="Eliminar Medicamento">   <button class="btn btn-danger btn-sm"><i class="fa fa-trash"></i></button></a></td> </tr>';
            }
            $("#store").html(asignacionBusquedahtml);
        }
    })
}); */

