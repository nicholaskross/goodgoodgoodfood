import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  title = 'Charity Cart';

  cart = [];
  constructor() { }

  ngOnInit() {
  }

  addToCart(item){
    this.cart.push(item)
  }

}
