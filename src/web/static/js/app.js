// This file contains the JavaScript logic for the frontend application, handling user interactions and API calls.

document.addEventListener('DOMContentLoaded', function() {
    const traceButton = document.getElementById('trace-button');
    const productIdInput = document.getElementById('product-id');
    const traceResult = document.getElementById('trace-result');

    traceButton.addEventListener('click', function() {
        const productId = productIdInput.value;
        fetch(`/api/trace/${productId}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    traceResult.innerHTML = JSON.stringify(data.traceInfo, null, 2);
                } else {
                    traceResult.innerHTML = 'Product not found.';
                }
            })
            .catch(error => {
                console.error('Error fetching trace information:', error);
                traceResult.innerHTML = 'Error fetching trace information.';
            });
    });

    const addProductButton = document.getElementById('add-product-button');
    addProductButton.addEventListener('click', function() {
        const productData = {
            name: document.getElementById('product-name').value,
            supplier: document.getElementById('product-supplier').value,
            quantity: document.getElementById('product-quantity').value
        };

        fetch('/api/products', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(productData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Product added successfully!');
            } else {
                alert('Error adding product: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error adding product:', error);
            alert('Error adding product.');
        });
    });
});