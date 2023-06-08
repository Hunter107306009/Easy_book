//for (let i = 1; i <= 7; i++) {
//  	document.getElementById("box_" + i).addEventListener("click", function() {
//    if (document.getElementById("box_" + i).checked) {
//      document.getElementById("sta_" + i + "-1").style.display = "none";
//      document.getElementById("sta_" + i + "-2").style.display = "block";
//    } else {
//      document.getElementById("sta_" + i + "-1").style.display = "block";
//      document.getElementById("sta_" + i + "-2").style.display = "none";
//    }
//  });
//}

//for (let i = 1; i <= 7; i++) {
//	if (document.getElementById("box_" + i).checked) {
//      document.getElementById("sta_" + i + "-1").style.display = "none";
//      document.getElementById("sta_" + i + "-2").style.display = "block";
//    } else {
//      document.getElementById("sta_" + i + "-1").style.display = "block";
//      document.getElementById("sta_" + i + "-2").style.display = "none";
//    }
//};

document.getElementById("index2").addEventListener("click", function() {
    window.open("./checkout.html", "_blank", "width=800,height=600");
});

document.getElementById("index3").addEventListener("click", function() {
    window.open("./blacklist.html", "_blank", "width=800,height=600");
});
