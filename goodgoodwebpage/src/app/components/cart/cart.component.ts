import {Component, Input, OnInit} from '@angular/core';
import {SearchService} from "../../services/search.service";
import {CharityService} from "../../services/charity.service";

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {

  moneySaved: number;
  @Input() cart;
  @Input() genericprods;

  constructor(private searchService: SearchService, private charityService: CharityService) { }

  ngOnInit() {
  }

  swapForGeneric(index){
    let sku = this.cart[index].sku;
    if(this.genericprods[sku]){
      let newprod = this.genericprods[sku];
      this.moneySaved += this.cart[index].price - newprod.price;
      this.cart[index] = newprod;
      this.charityService.changeAmountedDonated(this.moneySaved);
      this.charityService.changeCart(createSKUString());

    }
  }
  createSKUString(){
    skuCSV = '';
    for(let x = 0; x < cart.length; x++){
      if(x == 0){
        skuCSV = cart[x].sku
      }
      else{
        skuCSV += ',' + cart[x].sku
      }
    }
    return skuCSV
  }
}
