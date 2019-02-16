import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {

  cart: [];

  constructor() { }

  ngOnInit() {
    this.cart = [1,2,3,4,5];

  }

}
