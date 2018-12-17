var map;
var flightPathLine;
var markers = [];
$(function(){
  $('#origin').keyup(function(){
      var search = $('#origin').val();
      var url = "/search/" + search;
      var jqxhr = $.get( url, function(data) {
          var originSearch = $('#originSearch');
          originSearch.html("");
          for(var i = 0; i < data.length; i++){
              var airport = data[i];
              var htmlStr = "<a data-code='" + airport.LocationID  +"'>" + airport.LocationID + " -- " + airport.FacilityName + ", " + airport.City + ", " + airport.State + "</a>"
              var link = $($.parseHTML(htmlStr));
              link.click(function(event){
                   $("#origin").val($(this).attr('data-code'));
                   $('#originSearch').html("");
              });
              originSearch.append(link);
              originSearch.append($($.parseHTML("<br>")));
          }

      });
  });
  $('#destination').keyup(function(){
      var search = $('#destination').val();
      var url = "/search/" + search;
      var jqxhr = $.get( url, function(data) {
          var destinationSearch = $('#destinationSearch');
          destinationSearch.html("");
          for(var i = 0; i < data.length; i++){
              var airport = data[i];
              var htmlStr = "<a data-code='" + airport.LocationID  +"'>" + airport.LocationID + " -- " + airport.FacilityName + ", " + airport.City + ", " + airport.State + "</a>"
              var link = $($.parseHTML(htmlStr));
              link.click(function(event){
                   $("#destination").val($(this).attr('data-code'));
                   $('#destinationSearch').html("");
              });
              destinationSearch.append(link);
              destinationSearch.append($($.parseHTML("<br>")));
          }

      });
  });
  $("#submit").click(function(){
      $("#input").hide();
      var origin = $("#origin").val();
      var destination = $("#destination").val();
      var range = $("#range").val();
      var url = "/route/" + origin + "/" + destination + "/" + range;
      var htmlStr = "<img src='/loading.gif' width=12 height=12> Calculating. Please Wait... Origin: " + origin + " Destination: " + destination + " Range: " + range;
      $("#statusBar").show();
      $("#statusBar").html(htmlStr);
      var jqxhr = $.get( url, function(data) {
          var htmlStr = "Origin: " + origin + " Destination: " + destination + " Range: " + range;
          $("#statusBar").html(htmlStr);
          var resetBtn = $($.parseHTML("<input type='button' value='Reset'>"));
          resetBtn.click(function(){
              $("#statusBar").hide();
              $("#input").show();
              $("#origin").val('');
              $("#destination").val('');
              $("#range").val('');
              flightPathLine.setMap(null);
              for(var i = 0; i < markers.length; i++){
                markers[i].setMap(null);
              }
              markers.length = 0;
          });
          $("#statusBar").append(resetBtn);
          var flightPath = [];
          var getPin = function(node){
              url = "/airport/" + node[0];
              var airportData = $.get(url, function(data) {
                    var latLng = {lat: parseFloat(data.Latitude), lng: parseFloat(data.Longitude)};
                    flightPath.push(latLng);
                    var marker = new google.maps.Marker({
                        position: latLng,
                        map: map,
                        title: data.FacilityName
                    });
                    markers.push(marker);
                    if (flightPath.length > 0){
                        if (flightPathLine){
                            flightPathLine.setMap(null);
                        }
                        flightPathLine = new google.maps.Polyline({
                            path: flightPath,
                            geodesic: true,
                            strokeColor: '#00FF00',
                            strokeOpacity: 1.0,
                            strokeWeight: 2
                        });
                        flightPathLine.setMap(map);
                    }
                    if(node[1].length > 0){
                        getPin(node[1])
                    }
              });
          }
          getPin(data[1]);
      });
  })
});

function initMap() {
map = new google.maps.Map(document.getElementById('map'), {
  center: {lat: 38.83, lng: -97.6},
  zoom: 5
});
}