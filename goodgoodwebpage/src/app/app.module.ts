import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {
  MatCardModule,
  MatDividerModule,
  MatExpansionModule, MatFormFieldModule,
  MatGridListModule, MatInputModule,
  MatToolbarModule,
  MatListModule, MatButtonModule
} from "@angular/material";
import { NavbarComponent } from './components/navbar/navbar.component';
import { SearchFilterComponent } from './components/search-filter/search-filter.component';
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {CartComponent} from "./components/cart/cart.component";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import { CharitiesComponent } from './components/charities/charities.component';
import { HomeComponent } from './components/home/home.component';
import { FooterComponent } from './components/footer/footer.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    SearchFilterComponent,
    NavbarComponent,
    CartComponent,
    CharitiesComponent,
    HomeComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatToolbarModule,
    MatExpansionModule,
    BrowserAnimationsModule,
    MatCardModule,
    MatDividerModule,
    MatGridListModule,
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule,
    MatListModule,
    HttpClientModule,
    MatButtonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
