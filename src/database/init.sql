CREATE DATABASE algotrader;
GRANT ALL PRIVILEGES ON DATABASE algotrader TO postgres;
\connect algotrader;

CREATE SCHEMA binance;
CREATE SCHEMA interactive_brokers;

ALTER SCHEMA binance OWNER TO postgres;
ALTER SCHEMA interactive_brokers OWNER TO postgres;