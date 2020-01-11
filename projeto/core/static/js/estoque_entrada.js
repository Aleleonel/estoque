 $(document).ready(function() {
       $('#id_estoque-0-produto').addClass('clProduto');
       $('#id_estoque-0-quantidade').addClass('clQuantidade');

       $('#add-item').click(function(ev){
        console.log('Add item');
        ev.preventDefault();
        var count =$('#estoque').children().length;
        var tmplMarkup = $('#item-estoque').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('div#estoque').append(compiledTmpl);

        $('#id_estoque-TOTAL_FORMS').attr('value', count + 1);

        $('html, body').animate({
            scrollTop: $("#add-item").position().top - 200
        }, 800);
        $('#id_estoque-' + (count) + '-produto').addClass('clProduto');
        $('#id_estoque-' + (count) + '-quantidade').addClass('clQuantidade');
        });
    });

     let estoque
     let saldo
     let campo
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
                $('#' +campo).val('')
            },
            // Remove o valor do campo 'quantidade'
            error: function(xhr) {
                //body

            }
        })
     });

     $(document).on('change', '.clQuantidade', function() {
        quantidade = $(this).val();
        saldo = Number(quantidade) + Number(estoque);
        campo = $(this).attr('id').replace('quantidade', 'saldo');
        // Atribui o saldo ao campo 'saldo'
        $('#' +campo).val(saldo)
     });
