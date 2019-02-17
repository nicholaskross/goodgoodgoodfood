import {Component, Input, OnInit} from '@angular/core';
import {SearchService} from "../../services/search.service";
import {CharityService} from "../../services/charity.service";


@Component({
  selector: 'app-charities',
  templateUrl: './charities.component.html',
  styleUrls: ['./charities.component.scss']
})
export class CharitiesComponent implements OnInit {
  cart: any;
  moneySaved = 0;
  skuString: string;
  charities;

  constructor(private searchService: SearchService, private charityService: CharityService) {

    charityService.cartItems$.subscribe(
      data => {
        this.cart = data;
      }
    );
    this.charityService.moneyDonated$.subscribe(
      data => {
        console.log("A")
        console.log(data);
        this.moneySaved = data;
      }
    );

  }

  ngOnInit() {
    this.moneySaved = this.charityService.moneyDonated;
    this.cart = this.charityService.cartItems;

    this.searchService.charitySearch(this.cart).subscribe(
      data => {
        this.charities = data;
        console.log(this.charities);
      });
  }

}
