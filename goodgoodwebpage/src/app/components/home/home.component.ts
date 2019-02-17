import {Component, OnInit} from '@angular/core';
import {SearchService} from "../../services/search.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  title = 'Charity Cart';

  cart = [];
  alternatives = {};
  money_saved = [];

  constructor(private searchService: SearchService) {
  }

  ngOnInit() {
  }

  fetchAlternatives(sku: string) {
    console.log("search for " + sku);
    this.searchService.getGeneric(sku).subscribe(genericprod => {
      if (genericprod) {
        this.alternatives[sku] = genericprod;
        console.log("found ");
        console.log(genericprod);
      }
    });

  }

  addToCart(item) {
    this.cart.push(item);
    this.money_saved.push(0);
    this.fetchAlternatives(item.sku);
  }

}
