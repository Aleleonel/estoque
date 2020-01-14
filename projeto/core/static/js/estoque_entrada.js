 $(document).ready(function() {
   // Insere classe no primeiro item de produto
   $('#id_estoque-0-produto').addClass('clProduto');
   $('#id_estoque-0-quantidade').addClass('clQuantidade');
   // Desabilita o primeiro campo 'Saldo'
   $('#id_estoque-0-saldo').prop('type', 'hidden')
   // cria um span ṕara mostrar o saldo na tela
   $('label[for="id_estoque-0-saldo"]').append('<span id="id_estoque-0-saldo-span" class="lead" style="padding-left:10px;"></span>')
   // Select2
   $('.clProduto').select2()

 });

$('#add-item').click(function(ev){
    ev.preventDefault();
    var count =$('#estoque').children().length;
    var tmplMarkup = $('#item-estoque').html();
    var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
    $('div#estoque').append(compiledTmpl);

    // update form count
    $('#id_estoque-TOTAL_FORMS').attr('value', count + 1);

    // Desabilitar todos os campos 'Saldo'
    $('#id_estoque-' + (count) + '-saldo').prop('type', 'hidden')

    // cria um span ṕara mostrar o saldo na tela
    $('label[for="id_estoque-' + (count) + '-saldo"]').append('<span id="id_estoque-' + (count) + '-saldo-span" class="lead" style="padding-left:10px;"></span>')

    // some animate to scroll to view our new form
    $('html, body').animate({
       scrollTop: $("#add-item").position().top - 200
    }, 800);

    $('#id_estoque-' + (count) + '-produto').addClass('clProduto');
    $('#id_estoque-' + (count) + '-quantidade').addClass('clQuantidade');

    // cria um span para mostrar o saldo na tela
    $('label[for="id_estoque-' + (count) + '-saldo"]').append('<span id="id_estoque-' + (count) + '-saldo-span" class="lead" style="padding-left:10px;"></span>')

    // select2
    $('.clProduto').select2()
});


let estoque
let saldo
let campo
let campo2
let quantidade

$(document).on('change', '.clProduto', function(){
    let self = $(this)
    let pk = $(this).val()
    let url = '/produto/' + pk + '/json/'

$.ajax({
    url: url,
    type: 'GET',
    success: function(response){
        estoque = response.data[0].estoque
        campo = self.attr('id').replace('produto', 'quantidade')
       // Remove o valor do campo 'quantidade'
        $('#'+campo).val('')
    },
    error: function(xhr) {
        //body
    }
  })
});

$(document).on('change', '.clQuantidade', function() {
    quantidade = $(this).val();
    // Aqui é feito o cálculo de soma do estoque
    saldo = Number(quantidade) + Number(estoque);
    campo = $(this).attr('id').replace('quantidade', 'saldo');
    // Desabilita o 'Saldo'
    $('#' +campo).prop('type', 'hidden')
    // Atribui o saldo ao campo 'saldo'
    $('#' +campo).val(saldo)
    campo2 = $(this).attr('id').replace('quantidade', 'saldo-span')
    // Atribui o saldo ao campo 'id_estoque-x-saldo-span'
    $('#' +campo2).text(saldo)
});
