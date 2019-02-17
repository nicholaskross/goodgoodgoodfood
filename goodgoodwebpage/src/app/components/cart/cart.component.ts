import {Component, Input, OnInit} from '@angular/core';
import {SearchService} from "../../services/search.service";
import {CharityService} from "../../services/charity.service";

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {

  @Input() money_saved;
  @Input() cart;
  @Input() genericprods;

  constructor(private searchService: SearchService, private charityService: CharityService) { }

  ngOnInit() {
  }

  swapForGeneric(index){
    let sku = this.cart[index].sku;
    if(this.genericprods[sku]){
      let newprod = this.genericprods[sku];
      this.money_saved[index] = this.cart[index].price - newprod.price;
      this.cart[index] = newprod;
      this.charityService.changeAmountedDonated(this.totalSaved());
      this.charityService.changeCart(this.createSKUString());

    }
  }
  createSKUString(){
    let skuCSV = '';
    for(let x = 0; x < this.cart.length; x++){
      if(x == 0){
        skuCSV = this.cart[x].sku
      }
      else{
        skuCSV += ',' + this.cart[x].sku
      }
    }
    return skuCSV
  }

  totalSaved(){
    let total =0;
    for(let x of this.money_saved){
      total+=x
    }
    return total
  }
}
