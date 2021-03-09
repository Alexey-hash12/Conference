var map;
		var marker;
		function initMap ()
		  {
		  map = new ymaps.Map("yandexmap", {
		    center: [55.193114, 30.225111],
		    zoom: 14
		    });
		  marker = new ymaps.Placemark([55.193114, 30.225111], {
		    hintContent: 'Расположение',
		    balloonContent: 'Проспект Фрунзе, 35, корп.1'
		    });
		  map.geoObjects.add(marker);
		  }
		ymaps.ready(initMap);