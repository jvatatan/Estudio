// $(document).ready(function(){
//     $("buscar_dispositivoMedico").submit(function(e){
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

// $(document).ready(function(){
//     $("buscar_medicamento").submit(function(e){
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
function medicamento(){
    buscar_medicamento = document.getElementById("buscar_medicamento").value
    $.ajax({
        url:"/medicamentos/buscarMedicamento/",
        type:"GET",
        data:{
            asignacionColor : buscar_medicamento,
        },
        success: function(json){
            console.log("ntro");
            console.log(json);
           
        }
    })
}


var c = ' <tr role="row" class="odd" id="registro_item" style="background-color:rgb(255, 30, 30);"> <td style="color:Black;"><b>'+json[i].nomnre+'</b></td> <td style="color:Black;"><b>{{dispositivoMedico.fecha_vencimiento}}</b></td><td style="color:Black;"><b>{{dispositivoMedico.fabricado_por}}</b></td><td style="color:Black;"><b>{{dispositivoMedico.registro_invima}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.numero_lote}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.presentacion_comercial}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.forma_farmaceutica}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.principio_activo}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.unidad_medica}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.porcentaje}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.temperatura}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.riesgo}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.cantidad}}</b></td>
<td style="color:Black;"><b>{{dispositivoMedico.codigo}}</b></td>
<td style="background-color:rgb(255, 255, 255);">
</div>
</div>
<a href="{% url 'actualizarDispositivoMedico' dispositivoMedico.id %}"  data-toggle="tooltip" title="Actualizar Dispositivo Medicó">
  <button class="btn btn-primary btn-sm">
  <i class="fa fa-edit"></i>
  </button>
</a>
<a href="{% url 'eliminarDispositivoMedico' dispositivoMedico.id %}"  data-toggle="tooltip" title="Eliminar Dispositivo Medicó">
  <button class="btn btn-danger btn-sm">
  <i class="fa fa-trash"></i>
  </button>
</a>

</td>
</tr>'


$(function(){
    $('#store').empty();
    $.ajax({
        url: '/products/get_products_json/',
        type: 'GET',
        success: function (json) {
            var queryhtml = '';
            for (var i = 0; i < json.length; i++) {
                queryhtml += '<ul class="col-md-4 col-sm-6 col-xs-w"><li><div class="product product-single">			<div class="product-thumb"><a href="/products/view_product.html/' + json[i].id + '/"><button class="main-btn quick-view"><i class="fa fa-search-plus"></i> Vista previa</button></a><img src="../../../static/' + json[i].picture + '" class="img-fluid rounded " alt=""></div><div class="product-body"><h3 class="product-price">$ ' + json[i].name + ' </h3><h3 class="product-price">Categoria: ' + json[i].category + ' </h3>	<div class="product-rating">					<i class="fa fa-star"></i>					<i class="fa fa-star"></i>					<i class="fa fa-star"></i>					<i class="fa fa-star"></i>					<i class="fa fa-star-o empty"></i>				</div>				<h3 class="product-name"><a href="#">$ ' + json[i].value + '</a></h3>				<div class="product-btns">					<button class="main-btn icon-btn"><i class="fa fa-heart"></i></button>					<button class="main-btn icon-btn"><i class="fa fa-exchange"></i></button>					<button type="submit" class="primary-btn add-to-cart" id="{{product.id}}" onclick="getIdProductSelect(' + json[i].id + ')"><i class="fa fa-shopping-cart"></i> Agregar al carrito</button>				</div>			</div>		</div>	</li></ul>';
            }
            $("#store").html(queryhtml);
        }
    })
});