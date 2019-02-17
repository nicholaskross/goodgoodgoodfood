import { Injectable } from '@angular/core';
import {Subject} from "rxjs/index";

@Injectable({
  providedIn: 'root'
})
export class CharityService {

  private cartItemsSource = new Subject<any>();
  private moneyDonatedSource = new Subject<any>();

  cartItems$ = this.cartItemsSource.asObservable();
  moneyDonated$ = this.moneyDonatedSource.asObservable();

  changeCart(cart){
    this.cartItemsSource.next(cart)
  }
  changeAmountedDonated(donated){
    this.moneyDonatedSource.next(donated)
  }

  constructor() {}

}
