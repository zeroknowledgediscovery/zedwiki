  <h1>Listing /somedir</h1><!-- Custom Script (defered load, after dom ready) -->
  <script>
    $.getJSON('./', data => {
        console.log(data); //["doc1.jpg", "doc2.jpg", "doc3.jpg"] 
    });
  </script>
