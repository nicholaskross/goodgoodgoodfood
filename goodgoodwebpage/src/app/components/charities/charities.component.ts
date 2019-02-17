import {Component, Input, OnInit} from '@angular/core';
import {SearchService} from "../../services/search.service";
import {CharityService} from "../../services/charity.service";


@Component({
  selector: 'app-charities',
  templateUrl: './charities.component.html',
  styleUrls: ['./charities.component.scss']
})
export class CharitiesComponent implements OnInit {
  cart: any ;
  moneySaved;
  skuString: string;
  charities;

  constructor(private searchService: SearchService, private charityService: CharityService) {
      charityService.cartItems$.subscribe(
        data =>{
          this.cart = data;
        }
      );
      this.charityService.moneyDonated$.subscribe(
        data =>{
          this.moneySaved = data;
        }
      );

      this.searchService.charitySearch(this.skuString).subscribe(
        data=>{
          this.charities = data;

      });
  }

  ngOnInit() {
  }

}
