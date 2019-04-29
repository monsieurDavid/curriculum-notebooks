
$.getJSON("./data.json", function(json) {
    for (notebook in json) {
        let data = json[notebook];
        let info = `<li><h2>${data.Title}</h2> <p><b>Grade:</b> ${data.Grade} <b>Subject:</b> ${data.Subject}</p> <p>${data.Description}</p><a href="${data.Hyperlink}">Click here for Notebook</a></li>`
        $('#NotebookList').append(info);
    }

})
