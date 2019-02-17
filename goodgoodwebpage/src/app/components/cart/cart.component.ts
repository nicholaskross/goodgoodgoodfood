import {Component, Input, OnInit} from '@angular/core';
import {SearchService} from "../../services/search.service";

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {

  moneySaved: number;
  @Input() cart;
  @Input() genericprods;

  constructor(private searchService: SearchService) { }

  ngOnInit() {
  }

  swapForGeneric(index){
    console.log(this.cart[index].sku);
    this.searchService.getGeneric(this.cart[index].sku).subscribe(
      data => {
        if(data != null){ this.cart[index] = data}},
      error => {console.log(error)}
    )
  }
}
