/**
 * Created by chou6 on 2018-06-28.
 */
window.addEventListener('load', function () {
    document.getElementById('uploadbtn').addEventListener('click',uploadFile);

});
function uploadFile(){
//    var test = document.getElementById('test1');
    var file = document.getElementById('myFile');
    var filedata = new FormData(); // FormData 인스턴스 생성


    if (!file.value) return; // 파일이 없는 경우 빠져나오기

    filedata.append('uploadfile', file.files[0]);

    filedata.append('fileName', file.files[0].name);

//    filedata.append('test1', test.value)

    for (var pair of filedata.entries()) {
    console.log(pair[0]+ ', ' + pair[1]);
    }
    console.log(file);
        $.ajax({    
        url: 'index_upload/',
        type: 'POST',
        data: filedata,
        cache: false,
        processData: false, // essential
        contentType: false, // essential, application/pdf doesn't work.
        enctype: 'multipart/form-data',

        // If sucess, download file
        success: function(data, status, xhr) {
            console.log("success");
        }
    });

}