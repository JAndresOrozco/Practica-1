'use strict'

const Database = use('Database')

class UserController {

    async index (request, response) {
        return await Database
          .table('users')
      }
}

module.exports = UserController
