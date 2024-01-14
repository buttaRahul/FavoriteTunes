<div>
  <h3>Table of Contents:</h3>
  <ol>
    <li><a href="#">Installation</a></li>
    <li>
      <a href="#">Views</a>
      <ul>
        <li><a href="#aview">View for Artists List</a></li>
        <li><a href="#sview">View for Songs List</a></li>
        <li><a href="#cview">View for Catalog</a></li>
        <li><a href="#nartist">View for Adding New Artist</a></li>
        <li><a href="#nsong">View for Adding New Song</a></li>
        <li><a href="#asong">View for Artist's Songs</a></li>
      </ul>
    </li>
    <li><a href="#">Technicals</a></li>
  </ol>
  <h3>1.Installation:</h3>
  <p>
    <br>
    Clone the repository:
    <br>
      &nbsp &nbsp &nbsp git clone https://github.com/buttaRahul/FavoriteTunes.git
    <br>
    Navigate to the project directory:
    <br>
      &nbsp &nbsp &nbsp cd FaviruteTunes
    <br>
    Install dependencies:
     <br>
     &nbsp &nbsp &nbsp pip install -r requirements.txt
     <br>
    Apply migrations:
     <br>
     &nbsp &nbsp &nbsp python manage.py migrate
     <br>
    Create a superuser:
     <br>
     &nbsp &nbsp &nbsp python manage.py createsuperuser
     <br>
    Run the development server:
     <br>
     &nbsp &nbsp &nbsp python manage.py runserver
     
  </p>
  <h3>2.Views:</h3>
<!--   <img src></img> -->
<div id='aview' >
  <h5>View for Artists List</h5>
  <img src="images/artistview.png" alt="Artist List View">
</div>
<div id='sview' >
  <h5>View for Songs List</h5>
  <img src="images/songsview.png" alt="Songs List View">
</div>
<div id='cview' >
  <h5>View for Catalog</h5>
  <img src="images/catalogview.png" alt="Catalog View">
</div>
<div id='nartist' >
  <h5>View for Adding New Artist</h5>
  <img src="images/addartistview.png" alt="Add Artist View">
</div>
<div id='nsong' >
  <h5>View for Adding New Song</h5>
  <img src="images/addsongview.png" alt="Add Song View">
</div>
<div id='asong' >
  <h5>View for all Songs by Artist</h5>
  <img src="images/artistsongsview.png" alt="Artist Songs View">
</div>
</div>
