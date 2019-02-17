import {Component, Input, OnInit} from '@angular/core';
import {SearchService} from "../../services/search.service";

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {

  @Input() money_saved;
  @Input() cart;
  @Input() genericprods;

  constructor(private searchService: SearchService) { }

  ngOnInit() {
  }

  swapForGeneric(index){
    let sku = this.cart[index].sku;
    if(this.genericprods[sku]){
      let newprod = this.genericprods[sku];
      this.money_saved[index] = this.cart[index].price - newprod.price;
      this.cart[index] = newprod;
    }
  }
}
