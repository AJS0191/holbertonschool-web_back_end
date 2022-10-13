-- creates a trigger for items tables when a new order for an item comes in
-- it decreases its value in the items table
CREATE TRIGGER decrQuant AFTER INSERT ON orders FOR EACH ROW UPDATE items SET items.quantity = (items.quantity - NEW.number) WHERE items.name = NEW.item_name;
