import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  cart = [];
  addToCart(cartItem){
    console.log(cartItem);
    this.cart.push(cartItem)
  }
}
