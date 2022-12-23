
$('li.kit').click(function(){
    index = $(this).index()
    gp_name = $('a#kit_name_'+index).text()
    kit_id = $('span#'+index).text()
    $.ajax({
        url: '/get_tests/',
        method: 'get',
        dataType: 'json',
        csrfmiddlewaretoken: '{{ csrf_token }}',
        data: {'kit_id': kit_id},
        success: function(tests){
            $('.cls_hidden').hide(500);
            $('#set_test').empty()
            if (tests.length > 0){
                for (let i=0; i < tests.length; ++i){
                    current_test_name = tests[i].name
                    current_test_id = tests[i].id
                    $('#set_test').append('<div class="d-flex text-muted pt-3"><svg class="bd-placeholder-img flex-shrink-0 me-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 32x32" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#db0b0b"/></svg><div class="pb-3 mb-0 small lh-sm border-bottom w-100"><div class="d-flex justify-content-between"><strong class="text-gray-dark">'+ current_test_name +'</strong><a href="/check/' + current_test_id + '">Запустить</a></div><span class="d-block">Группа: ' + gp_name + '</span></div></div>')
                };
               }
            else {
                $('#set_test').append('<b>тестов пока нет</b>')
            };
            $('.cls_hidden').show('slow')
        }
    });
});

$(".pane-list li").click(function(){
    window.location=$(this).find("a").attr("href"); return false;
});