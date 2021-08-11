import { TestBed } from '@angular/core/testing';

import { AuthVGuard } from './auth-v.guard';

describe('AuthVGuard', () => {
  let guard: AuthVGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(AuthVGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
