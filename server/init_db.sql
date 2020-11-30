USE datarepresentation; /* activate database */

CREATE TABLE equipment (
  id INT PRIMARY KEY AUTO_INCREMENT,
  category ENUM('Tier 1', 'Tier 2', 'Auxiliary', 'Spare') DEFAULT 'Tier 1',
  name VARCHAR(50),
  supplier VARCHAR(50),
  price_eur FLOAT(10, 2),
  price_bc FLOAT(8, 4)
);
