document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('searchCategoriaDropdown'); // Cambio de id
    const lista = document.getElementById('listaCategoriasDropdown'); // Cambio de id

    if (input && lista) {
        input.addEventListener('input', () => {
            const filter = input.value.toLowerCase();
            const items = lista.querySelectorAll('li');

            items.forEach(item => {
                const text = item.textContent.toLowerCase();
                item.style.display = text.includes(filter) ? '' : 'none';
            });
        });
    }
});
