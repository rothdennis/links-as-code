function searchLinks() {
    // get the search query from the input field
    var input = document.getElementById("search");
    var filter = input.value.toLowerCase();
    console.log(filter);

    // get all div with class "group"
    var groups = document.getElementsByClassName("group");

    // loop through all groups    
    for (var i = 0; i < groups.length; i++) {
        var group = groups[i];
        var links = group.getElementsByTagName("a");
        var groupMatches = false;

        // loop through all links in the group
        for (var j = 0; j < links.length; j++) {
            var link = links[j];
            var text = link.textContent || link.innerText;

            // check if the link text matches the search query
            if (text.toLowerCase().indexOf(filter) > -1) {
                link.style.display = "";
                groupMatches = true;
            } else {
                link.style.display = "none";
            }
        }

        // show or hide the group based on whether any links matched
        if (groupMatches) {
            group.style.display = "";
        } else {
            group.style.display = "none";
        }
    } 
    
}