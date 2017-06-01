function JsImgDown() {
    // Queries page for all elements and initializes the global variables
    var elems = document.querySelectorAll('*');
    var elems2 = document.querySelectorAll('img');
    var images = {};
    var href = "";

    // Queries for the CSS bankground image
    for (var a = 0; a < elems.length; a++) {
        var style = elems[a].currentStyle || window.getComputedStyle(elems[a], false);
        var background = style.backgroundImage.slice(4, -1);
        if (background) {
            images[background] = background;
        }
    }
    
    // Retrieves all the <img src="*" />
    for (var a = 0; a < elems2.length; a++) {
        if (href = elems2[a].getAttribute('src'))
            images[href] = href;
    }

    // Generate an <a> tag and initialize downloading, then remove the link
    for (var i in images) {
        var link = document.createElement('a');

        link.setAttribute('download', '');
        link.setAttribute('href', i);
        link.click();

        delete link;
    }
}

JsImgDown();