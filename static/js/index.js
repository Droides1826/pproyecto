document.addEventListener('DOMContentLoaded', () => {
    const scriptTag = document.querySelector('script[data-endpoint]');
    const endpoint = scriptTag.getAttribute('data-endpoint');

    fetch(endpoint) // Ruta de tu API
        .then(response => response.json())
        .then(data => {
            const container = document.querySelector('.producto-container');
            container.innerHTML = ''; // Limpiar el contenedor antes de agregar nuevos productos
            data.forEach(producto => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('hogar');
                
                productDiv.innerHTML = `
                    <img class="imagen" src="/static/uploads/${producto.nombre_imagen}" alt="">
                    <div class="card-hogar">
                        <h1 class="title1">${producto.nombre}</h1>
                        <p>${producto.descripcion}</p>
                        <a class="ver-mas-btn" href="/categoria/${producto.id_categoria}?producto_id=${producto.id_producto}" data-nombre="${producto.nombre}" data-imagen="/static/uploads/${producto.nombre_imagen}" data-descripcion="${producto.descripcion}" data-precio="${producto.precio}">Más información aqui</a>
                    </div>
                `;
                container.appendChild(productDiv);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});