// var csrftoken = $.cookie('csfrtoken');
var csrftoken  = $('input[name="csrfmiddlewaretoken"]').val();
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$("#search_ajax").click(function(){
    var url = $("#TransactionForm").attr("search-transaction-url");
    valor = $("#id_querycom").val();
    console.log(valor);
    console.log(url);
    respuestatransaction(valor,url)
});
function respuestatransaction(valor,url) {
    $.ajax({
        beforeSend : function(xhr, settings) {
            if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        url : url,
        type : "GET",
        data : {valor : valor},
        success: function(data){      

            valor_retornado = 
            
            "<div class='modal fade' id='mostrarmodal' tabindex='-1' role='dialog' aria-labelledby='exampleModalLongTitle' style='padding-right: 17px; display: block;' aria-modal='true'><div class='modal-dialog' role='document'><div class='modal-content'><div class='modal-header'><h5 class='modal-title' id='exampleModalLongTitle'>"+data[0].title+"</h5><button type='button' class='btn-close' data-bs-dismiss='modal' aria-label='Close'><span aria-hidden='true'></span></button></div><div class='modal-body'><h6>Wallet:</h6>"+data[0].wallet+"</div><div class='modal-body'><h6>Date:</h6>"+data[0].date+"</div><div class='modal-body'><h6>Type Transaction:</h6>"+data[0].typeTransaction+"</div><div class='modal-body'><h6>SubCategoryTransaction:</h6>"+data[0].subCategoryTransaction+"</div><div class='modal-body'><h6>Description:</h6>"+data[0].description+"</div><div class='modal-body'><h6>Amount:</h6>"+data[0].amount+"</div><div class='modal-footer'><button type='button' class='btn btn-secondary' data-bs-dismiss='modal'>Cerrar</button></div></div></div></div>"                               
            
            $("#contenedor_filtrado").html(valor_retornado);
            console.log(data);
            $("#mostrarmodal").modal("show");
        },
        error : function(xhr, errmsg, err) {
            console.log("Error trying to response");
        },
    });
}