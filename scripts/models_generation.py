import os

template = r"""<?php

require_once 'ConnectionClass.php';

class {model_name} extends Database
{
  private $id;
  {private_properties}
  private $table = "{table_name}";

  public function __construct($id = null)
  {
    $this->conn = $this->getConnection();

    if ($id) {
      $this->findById($id);
    }
  }

  private function findById($id)
  {
    $sql = "SELECT * FROM {$this->table} WHERE id = :id";

    try {
      $stmt = $this->conn->prepare($sql);
      $stmt->bindParam(':id', $id, PDO::PARAM_INT);
      $stmt->execute();

      $record = $stmt->fetch(\PDO::FETCH_ASSOC);

      if ($record) {
        foreach ($record as $key => $value) {
          $this->{"set" . ucfirst($key)}($value);
        }
      }
    } catch (\PDOException $e) {
      throw new \PDOException($e->getMessage());
    }
  }

  public function current()
  {
    $data = new stdClass();
    $data->id = $this->getId();
    {current_properties}
    return $data;
  }

  public function totalCount($filters = [])
  {
    $sql = "SELECT COUNT(id) as total FROM {$this->table}";

    if (!empty($filters)) {
      $sql .= " WHERE ";
      $sql .= implode(" AND ", array_map(function ($column) {
        return "$column = :$column";
      }, array_keys($filters)));
    }

    try {
      $stmt = $this->conn->prepare($sql);

      if (!empty($filters)) {
        foreach ($filters as $column => $value) {
          $stmt->bindValue(":$column", $value);
        }
      }

      $stmt->execute();

      return $stmt->fetch(\PDO::FETCH_ASSOC);
    } catch (\PDOException $e) {
      throw new \PDOException($e->getMessage());
    }
  }

  public function find($filters = [], $limit = null, $offset = null, $order = [])
  {
    $sql = "SELECT * FROM {$this->table}";

    if (!empty($filters)) {
      $sql .= " WHERE ";
      $sql .= implode(" AND ", array_map(function ($column) {
        return "$column = :$column";
      }, array_keys($filters)));
    }

    if (!empty($order)) {
      $orderClauses = [];
      $direction = strtoupper($order['direction']) === 'DESC' ? 'DESC' : 'ASC';
      foreach ($order['cols'] as $column) {
        $orderClauses[] = "$column $direction";
      }
      $sql .= " ORDER BY " . implode(", ", $orderClauses);
    }

    if ($limit !== null) {
      $sql .= " LIMIT :limit";
    }

    if ($offset !== null) {
      $sql .= " OFFSET :offset";
    }

    try {
      $stmt = $this->conn->prepare($sql);

      if (!empty($filters)) {
        foreach ($filters as $column => $value) {
          $stmt->bindValue(":$column", $value);
        }
      }

      if ($limit !== null) {
        $stmt->bindValue(':limit', (int) $limit, PDO::PARAM_INT);
      }

      if ($offset !== null) {
        $stmt->bindValue(':offset', (int) $offset, PDO::PARAM_INT);
      }

      $stmt->execute();

      return $stmt->fetchAll(\PDO::FETCH_ASSOC);
    } catch (\PDOException $e) {
      throw new \PDOException($e->getMessage());
    }
  }

  public function create($data)
  {
    $sql = "INSERT INTO {$this->table} ({columns}) 
            VALUES ({values})";

    try {
      $stmt = $this->conn->prepare($sql);
      foreach ($data as $key => $value) {
        $stmt->bindValue(":$key", $value);
      }
      $stmt->execute();

      $this->findById($this->conn->lastInsertId());
      return $this->current();
    } catch (\PDOException $e) {
      throw new \PDOException($e->getMessage());
    }
  }

  public function update($data)
  {
    $sql = "UPDATE {$this->table} SET
            {update_columns}
            WHERE id = :id";

    foreach ($data as $column => $value) {
      $this->$column = $value;
    }

    try {
      $stmt = $this->conn->prepare($sql);
      $stmt->bindParam(':id', $this->id);
      {bind_params}
      $stmt->execute();

      $this->findById($this->id);
      return $this->current();
    } catch (\PDOException $e) {
      throw new \PDOException($e->getMessage());
    }
  }

  public function delete($id)
  {
    $sql = "DELETE FROM {$this->table} WHERE id = :id";

    try {
      $stmt = $this->conn->prepare($sql);
      $stmt->bindParam(':id', $id, PDO::PARAM_INT);
      $stmt->execute();
    } catch (\PDOException $e) {
      throw new \PDOException($e->getMessage());
    }
  }

  // Getters and Setters

  public function getId()
  {
    return $this->id;
  }

  public function setId($id)
  {
    $this->id = $id;
    return $this;
  }

  {getters_setters}
}
"""

def generate_model(table_name, columns):
    model_name = ''.join([word.capitalize() for word in table_name.split('_')]) + 'Model'
    private_properties = '\n  '.join([f'private ${col};' for col in columns])
    current_properties = '\n    '.join([f'$data->{col} = $this->get{col.capitalize()}();' for col in columns if col != 'id'])
    columns_str = ', '.join(columns)
    values_str = ', '.join([f':{col}' for col in columns])
    update_columns = ',\n            '.join([f'{col} = :{col}' for col in columns if col != 'id'])
    bind_params = '\n      '.join([f'$stmt->bindParam(\':{col}\', $this->{col});' for col in columns if col != 'id'])
    getters_setters = '\n\n  '.join([f'public function get{col.capitalize()}()\n  {{\n    return $this->{col};\n  }}\n\n  public function set{col.capitalize()}(${col})\n  {{\n    $this->{col} = ${col};\n    return $this;\n  }}' for col in columns])

    model_content = template.format(
        model_name=model_name,
        private_properties=private_properties,
        table_name=table_name,
        current_properties=current_properties,
        columns=columns_str,
        values=values_str,
        update_columns=update_columns,
        bind_params=bind_params,
        getters_setters=getters_setters
    )

    file_name = f'{model_name}.php'
    with open(file_name, 'w') as file:
        file.write(model_content)

    print(f'Model {model_name} generated successfully as {file_name}')

if __name__ == "__main__":
    table_name = input("Enter the table name: ")
    columns_input = input("Enter the columns separated by commas: ")
    columns = [col.strip() for col in columns_input.split(',')]
    generate_model(table_name, columns)