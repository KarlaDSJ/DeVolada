import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioComponent } from './modules/inicio/inicio.component';
import { ProductoComponent } from './modules/producto/producto.component';
import { CarritoComponent } from './modules/carrito/carrito.component';
import { DireccionComponent } from './modules/direccion/direccion.component';
import { MetodoPagoComponent } from './modules/metodo-pago/metodo-pago.component';
import { MisProductosComponent } from './modules/mis-productos/mis-productos.component';
import { CompraFinalizadaComponent } from './modules/compra-finalizada/compra-finalizada.component';
import { CrearResenaComponent } from './modules/crear-resena/crear-resena.component';
import { VerResenasComponent } from './modules/ver-resenas/ver-resenas.component';
import { LoginComponent } from './modules/login/login.component';
import { RegistrarComponent } from './modules/registrar/registrar.component';
import { AuthGuard } from './guard/auth.guard';
import { DireccionGuard } from './guard/direccion.guard';
import { MetodoPagoGuard } from './guard/metodo-pago.guard';
import { CompraFinalizadaGuard } from './guard/compra-finalizada.guard';

const routes: Routes = [
  {path: 'registrar', component: RegistrarComponent},
  {path:  '', component: LoginComponent},
  {path: 'carrito', component: CarritoComponent, canActivate:[AuthGuard]},
  {path: 'metodo-pago', component: MetodoPagoComponent, canActivate:[AuthGuard, MetodoPagoGuard]},   
  {path: 'inicio', component: InicioComponent, canActivate:[AuthGuard]},
  {path: 'producto/:id', component: ProductoComponent, canActivate:[AuthGuard]}, //Lleva el id de producto
  {path: 'direccion', component: DireccionComponent, canActivate:[AuthGuard, DireccionGuard]},
  {path: 'mis-productos', component: MisProductosComponent, canActivate:[AuthGuard]},
  {path: 'compra-finalizada/:idCompra', component: CompraFinalizadaComponent, canActivate:[AuthGuard, CompraFinalizadaGuard]},
  {path: 'crear-resena', component: CrearResenaComponent, canActivate:[AuthGuard]},
  {path: 'ver-resenas', component: VerResenasComponent, canActivate:[AuthGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
