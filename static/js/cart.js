// const increaseButtons = document.querySelectorAll(".increase-quantity");
// const decreaseButtons = document.querySelectorAll(".decrease-quantity");

// increaseButtons.forEach((button) => {
//     button.addEventListener("click", (event) => {
//         event.preventDefault();
//         const currentItem = event.target.closest(".cart-item");
//         const quantityElement = currentItem.querySelector(".item-quantity");
//         const priceElement = currentItem.querySelector(".cart-item-price");
//         const pricePerItem = parseFloat(priceElement.getAttribute("data-price"));
//         let currentQuantity = parseInt(quantityElement.textContent);

//         currentQuantity++;
//         quantityElement.textContent = currentQuantity;
//         updateCartItemPrice(priceElement, pricePerItem, currentQuantity);
//     });
// });

// decreaseButtons.forEach((button) => {
//     button.addEventListener("click", (event) => {
//         event.preventDefault();
//         const currentItem = event.target.closest(".cart-item");
//         const quantityElement = currentItem.querySelector(".item-quantity");
//         const priceElement = currentItem.querySelector(".cart-item-price");
//         const pricePerItem = parseFloat(priceElement.getAttribute("data-price"));
//         let currentQuantity = parseInt(quantityElement.textContent);

//         if (currentQuantity > 1) {
//             currentQuantity--;
//             quantityElement.textContent = currentQuantity;
//             updateCartItemPrice(priceElement, pricePerItem, currentQuantity);
//         }
//     });
// });

// function updateCartItemPrice(priceElement, pricePerItem, quantity) {
//     const totalPrice = (pricePerItem * quantity).toFixed(2);
//     priceElement.textContent = "Rs:" + totalPrice;

     
// }


const increaseButtons = document.querySelectorAll(".increase-quantity");
const decreaseButtons = document.querySelectorAll(".decrease-quantity");

increaseButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.preventDefault();
        const currentItem = event.target.closest(".cart-item");
        const quantityElement = currentItem.querySelector(".item-quantity");
        const priceElement = currentItem.querySelector(".cart-item-price");
        const pricePerItem = parseFloat(priceElement.getAttribute("data-price"));
        let currentQuantity = parseInt(quantityElement.textContent);

        currentQuantity++;
        quantityElement.textContent = currentQuantity;
        updateCartItemPrice(priceElement, pricePerItem, currentQuantity);

        // Update the checkout after the quantity changes
        updateCheckout();
    });
});

decreaseButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.preventDefault();
        const currentItem = event.target.closest(".cart-item");
        const quantityElement = currentItem.querySelector(".item-quantity");
        const priceElement = currentItem.querySelector(".cart-item-price");
        const pricePerItem = parseFloat(priceElement.getAttribute("data-price"));
        let currentQuantity = parseInt(quantityElement.textContent);

        if (currentQuantity > 1) {
            currentQuantity--;
            quantityElement.textContent = currentQuantity;
            updateCartItemPrice(priceElement, pricePerItem, currentQuantity);

            // Update the checkout after the quantity changes
            updateCheckout();
        }
    });
});

function updateCartItemPrice(priceElement, pricePerItem, quantity) {
    const totalPrice = (pricePerItem * quantity).toFixed(2);
    priceElement.textContent = "$" + totalPrice;
}

function updateCheckout() {
    // Fetch updated data from the cart page
    const cartItems = document.querySelectorAll(".cart-item");
    let totalAmount = 0;

    cartItems.forEach((item) => {
        const price = parseFloat(item.querySelector(".cart-item-price").getAttribute("data-price"));
        const quantity = parseInt(item.querySelector(".item-quantity").textContent);
        totalAmount += price * quantity;
    });

    // Update total amount in the checkout page
    const totalItemAmount = document.getElementById("total_item_amount");
    totalItemAmount.textContent = totalAmount.toFixed(2);
}



