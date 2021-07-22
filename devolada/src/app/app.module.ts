import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CarritoComponent } from './carrito/carrito.component';
import { MetodoPagoComponent } from './metodo-pago/metodo-pago.component';

@NgModule({
  declarations: [
    AppComponent,
    CarritoComponent,
    MetodoPagoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    FormsModule // Para las entradas (inputs) o formularios
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
