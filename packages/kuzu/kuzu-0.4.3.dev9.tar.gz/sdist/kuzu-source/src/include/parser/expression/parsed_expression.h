#pragma once

#include <memory>
#include <string>
#include <unordered_map>
#include <vector>

#include "common/cast.h"
#include "common/copy_constructors.h"
#include "common/enums/expression_type.h"

namespace kuzu {

namespace common {
struct FileInfo;
class Serializer;
class Deserializer;
} // namespace common

namespace parser {

class ParsedExpression;
class ParsedExpressionChildrenVisitor;
using parsed_expr_vector = std::vector<std::unique_ptr<ParsedExpression>>;
using parsed_expr_pair =
    std::pair<std::unique_ptr<ParsedExpression>, std::unique_ptr<ParsedExpression>>;
using s_parsed_expr_pair = std::pair<std::string, std::unique_ptr<ParsedExpression>>;

class ParsedExpression {
    friend class ParsedExpressionChildrenVisitor;

public:
    ParsedExpression(common::ExpressionType type, std::unique_ptr<ParsedExpression> child,
        std::string rawName);
    ParsedExpression(common::ExpressionType type, std::unique_ptr<ParsedExpression> left,
        std::unique_ptr<ParsedExpression> right, std::string rawName);
    ParsedExpression(common::ExpressionType type, std::string rawName)
        : type{type}, rawName{std::move(rawName)} {}
    explicit ParsedExpression(common::ExpressionType type) : type{type} {}

    ParsedExpression(common::ExpressionType type, std::string alias, std::string rawName,
        parsed_expr_vector children)
        : type{type}, alias{std::move(alias)}, rawName{std::move(rawName)},
          children{std::move(children)} {}
    DELETE_COPY_DEFAULT_MOVE(ParsedExpression);
    virtual ~ParsedExpression() = default;

    inline common::ExpressionType getExpressionType() const { return type; }

    inline void setAlias(std::string name) { alias = std::move(name); }

    inline bool hasAlias() const { return !alias.empty(); }

    inline std::string getAlias() const { return alias; }

    inline std::string getRawName() const { return rawName; }

    inline uint32_t getNumChildren() const { return children.size(); }
    inline ParsedExpression* getChild(uint32_t idx) const { return children[idx].get(); }

    inline std::string toString() const { return rawName; }

    virtual inline std::unique_ptr<ParsedExpression> copy() const {
        return std::make_unique<ParsedExpression>(type, alias, rawName, copyChildren());
    }

    void serialize(common::Serializer& serializer) const;

    static std::unique_ptr<ParsedExpression> deserialize(common::Deserializer& deserializer);

    template<class TARGET>
    const TARGET& constCast() const {
        return common::ku_dynamic_cast<const ParsedExpression&, const TARGET&>(*this);
    }
    template<class TARGET>
    const TARGET* constPtrCast() const {
        return common::ku_dynamic_cast<const ParsedExpression*, const TARGET*>(this);
    }

protected:
    parsed_expr_vector copyChildren() const;

private:
    virtual inline void serializeInternal(common::Serializer&) const {}

protected:
    common::ExpressionType type;
    std::string alias;
    std::string rawName;
    parsed_expr_vector children;
};

using options_t = std::unordered_map<std::string, std::unique_ptr<parser::ParsedExpression>>;

} // namespace parser
} // namespace kuzu
