# Discord API Reference

## Using Discord API Documentation

This project communicates with Discord's API endpoints. The official API documentation is maintained by Discord and serves as the authoritative reference for all available endpoints, their parameters, and responses.

### Official API Documentation Repository

**Repository:** [discord/discord-api-docs](https://github.com/discord/discord-api-docs)

This repository contains the complete specification of Discord's REST API and Gateway endpoints. When implementing or updating features in this project, always reference this documentation to ensure:

- Correct endpoint paths
- Proper request/response structures
- Valid HTTP methods
- Required permissions
- Rate limiting considerations

### Key Documentation Sections

- **REST API:** `/docs/resources` - Resource definitions and endpoint specifications
- **Gateway:** `/docs/topics/Gateway.md` - WebSocket gateway documentation
- **OAuth2:** `/docs/topics/OAuth2.md` - Authentication flows
- **Rate Limits:** `/docs/topics/Rate_Limits.md` - Rate limiting guidelines
- **Permissions:** `/docs/topics/Permissions.md` - Permission calculations

### Workflow for Implementation

1. **Check API Docs First:** Before implementing any Discord API feature, review the official documentation at <https://github.com/discord/discord-api-docs>
2. **Verify Endpoint Availability:** Ensure the endpoint exists and check for any deprecation notices
3. **Review Parameters:** Confirm required and optional parameters, types, and constraints
4. **Check Permissions:** Verify required bot permissions and OAuth2 scopes
5. **Consider Rate Limits:** Plan implementation to respect Discord's rate limits

### Keeping Up-to-Date

The Discord API evolves over time. To stay current:

- Watch the [discord-api-docs](https://github.com/discord/discord-api-docs) repository for updates
- Check the [changelog](https://github.com/discord/discord-api-docs/blob/main/docs/Change_Log.md)
- Subscribe to Discord's developer announcements

### API Versioning

Discord uses API versioning in the endpoint path (e.g., `/api/v10/`). This project should target the latest stable API version. Check the documentation for the current recommended version.

### Reference Links

- **GitHub Repository:** <https://github.com/discord/discord-api-docs>
- **Online Documentation:** <https://discord.com/developers/docs/intro>
- **Developer Portal:** <https://discord.com/developers/applications>

---

When in doubt about any API behavior or endpoint specification, the discord-api-docs repository is the single source of truth.
