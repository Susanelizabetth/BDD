Feature: Transacción bancaria
 Prueba relacionada con transacciones bancarias como retiro, depósito, transferencia, etc.

    Scenario: Deposito de dinero
        Given: El saldo de la cuenta es 100
        When: El titular retira 30
        Then: El saldo de la cuenta es 70

