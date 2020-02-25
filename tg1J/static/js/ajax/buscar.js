$(document).ready(function(){
    $("buscar_dispositivoMedico").submit(function(e){
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            success: function(json){
                console.log(json)
            }
        })
    })
})

$(document).ready(function(){
    $("buscar_medicamento").submit(function(e){
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            success: function(json){
                console.log(json)
            }
        })
    })
})

$(document).ready(function(e){
    $("buscar_perfilUsuario").submit(function(e){
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            success: function(json){
                console.log(json)
            }
        })
    })
})