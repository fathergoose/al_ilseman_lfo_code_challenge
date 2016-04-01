#!/usr/bin/env ruby

require 'sinatra'
require 'json'

def rate_customer(*args)
  old_and_rich = args[0].to_i * args[2].to_i / 100
  old_and_rich
end


get '/customer_scoring' do
  ranks = ["A","B","C","D","F"]
  income = params['income']
  zipcode = params['zipcode']
  age = params['age']
  propensity = rate_customer(income, zipcode, age)
  ranking = ranks[rand(5)]
  content_type :json
  { propensity: propensity.to_s, ranking: ranking }.to_json
end
